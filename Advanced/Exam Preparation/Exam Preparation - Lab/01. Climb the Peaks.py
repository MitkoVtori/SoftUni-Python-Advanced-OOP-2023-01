from collections import deque


def conquer_peaks(food, stamina):
    peaks = {"Vihren": 80, "Kutelo": 90, "Banski Suhodol": 100, "Polezhan": 60, "Kamenitza": 70}
    conquered_peaks = []

    day = 0

    while len(food) and len(stamina):

        if day == 7:
            break

        if not len(peaks):
            break

        day += 1
        daily_energy = food.pop() + stamina.popleft()
        current_peak = list(peaks.keys())[0]

        if daily_energy >= peaks[current_peak]:
            conquered_peaks.append(current_peak)
            del peaks[current_peak]

    return conquered_peaks


food_portions = deque(map(int, input().split(", ")))
stamina = deque(map(int, input().split(", ")))

conquered_peaks = conquer_peaks(food_portions, stamina)

if len(conquered_peaks) == 5:
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")

else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")

if conquered_peaks:
    print("Conquered peaks:")
    [print(peak) for peak in conquered_peaks]