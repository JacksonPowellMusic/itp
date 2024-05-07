import numpy as np
import mido
import random

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def intersection_of_intervals(intervals):
    if not intervals:
        return None
    current_lcm = intervals[0][0]
    current_start = intervals[0][1]
    for modulus, start in intervals[1:]:
        current_lcm = lcm(current_lcm, modulus)
        adjustment_found = False
        for i in range(modulus):
            new_start = (current_start + i * (current_lcm // modulus)) % current_lcm
            if (new_start - start) % modulus == 0:
                current_start = new_start
                adjustment_found = True
                break
        if not adjustment_found:
            return None
    return current_lcm, current_start

def generate_points(modulus, start, count=30):
    return [start + modulus * i for i in range(count)]

def get_distribution(prompt):
    print("\n" + prompt)
    print("1: Exponential")
    print("2: Linear (uniform)")
    print("3: Normal (Gaussian)")
    print("4: Binomial")
    print("5: Poisson")
    print("6: Arbitrary value")
    choice = input("Enter your choice (1-6): ")
    
    if choice == '1':
        scale = float(input("Enter the scale parameter for the exponential distribution: "))
        return lambda: min(127, max(0, int(np.random.exponential(scale))))
    elif choice == '2':
        min_val, max_val = map(float, input("Enter the min and max values for the uniform distribution: ").split())
        return lambda: min(127, max(0, int(random.uniform(min_val, max_val))))
    elif choice == '3':
        mu, sigma = map(float, input("Enter the mean (mu) and standard deviation (sigma) for the normal distribution: ").split())
        return lambda: min(127, max(0, int(np.random.normal(mu, sigma))))
    elif choice == '4':
        n, p = map(float, input("Enter the number of trials (n) and probability of success (p) for the binomial distribution: ").split())
        return lambda: min(127, max(0, int(np.random.binomial(n, p))))
    elif choice == '5':
        lam = float(input("Enter lambda for the Poisson distribution: "))
        return lambda: min(127, max(0, int(np.random.poisson(lam))))
    elif choice == '6':
        value = int(input("Enter an arbitrary fixed value: "))
        return lambda: min(127, max(0, value))
    else:
        print("Invalid choice, defaulting to arbitrary fixed value of 60.")
        return lambda: 60

def create_midi_from_sieve(modulus, start, note_func, velocity_func, duration_func, filename):
    mid = mido.MidiFile()
    track = mido.MidiTrack()
    mid.tracks.append(track)

    points = generate_points(modulus, start)
    last_time = 0
    for point in points:
        note = note_func()
        velocity = velocity_func()
        duration = duration_func()
        track.append(mido.Message('note_on', note=note, velocity=velocity, time=last_time))  # time is cumulative here
        track.append(mido.Message('note_off', note=note, velocity=velocity, time=duration))  # duration till note off
        last_time += duration

    mid.save(filename)
    print(f"MIDI file '{filename}' generated with complex parameter distributions.")

if __name__ == "__main__":
    print("Welcome to MIDI generation setup.")
    num_intervals = int(input("How many intervals would you like to input? "))
    intervals = []
    for i in range(num_intervals):
        modulus = int(input(f"Enter modulus for interval {i+1}: "))
        start = int(input(f"Enter start for interval {i+1}: "))
        intervals.append((modulus, start))

    result = intersection_of_intervals(intervals)
    if result:
        modulus, start = result
        print("Intersection found. Setting up distributions for MIDI parameters...")
        note_func = get_distribution("Select the distribution for MIDI note pitches")
        velocity_func = get_distribution("Select the distribution for MIDI note velocities")
        duration_func = get_distribution("Select the distribution for note durations (in ticks)")
        filename = input("Enter the filename for the output MIDI file (e.g., 'mymusic.mid'): ")
        create_midi_from_sieve(modulus, start, note_func, velocity_func, duration_func, filename)
    else:
        print("No valid intersection could be found.")
