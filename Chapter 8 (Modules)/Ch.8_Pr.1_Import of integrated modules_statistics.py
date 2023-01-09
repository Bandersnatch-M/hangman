# Chapter 8. Modules
# Practice challenge 1. 

print("""Вызовите различные функции из модуля statistics для ряда:
[1, 2, 3, 5, 73, 33, 64, 12, 46, 73, 33, 8, 2]
""")

print("Результат:")
import statistics
# Задаём числовой ряд
nums = [1, 2, 3, 5, 73, 33, 64, 12, 46, 73, 33, 8, 2]
print("Перечень значений статистических данных:")
# Среднее
print("Среднее арифметическое (mean)")
print(statistics.mean(nums))
# Среднее с плавающей точкой
print("Среднее арифметическое с плавающей точкой (float mean)")
print(statistics.fmean(nums))
# Геометрическое среднее
print("Геометрическое среднее (geometric mean)")
print(statistics.geometric_mean(nums))
# Гармоническое среднее
print("Гармоническое среднее (harmonic mean)")
print(statistics.harmonic_mean(nums))
# Медианы средняя, низкая, высокая
print("Медианы средняя, низкая, высокая")  
print(statistics.median(nums))
print(statistics.median_low(nums))
print(statistics.median_high(nums))
# Медиана групповая (Median, or 50th percentile, of grouped data)
print("Медиана групповая (Median, or 50th percentile, of grouped data)") 
print(statistics.median_grouped(nums)) 
# Мода
print("Мода (mode)")
print(statistics.mode(nums))
# Мультимода
print("Мультимода (multimode)")
print(statistics.multimode(nums))
# Quantiles (Divide data into intervals with equal probability.)
print("Quantiles (Divide data into intervals with equal probability.)")
print(statistics.quantiles(nums))

print("Перечень значений статистического распределения:")
# Population standard deviation of data
print("Population standard deviation of data (pstdev)")
print(statistics.pstdev(nums))
# Population variance of data
print("Population variance of data (pvariance)")
print(statistics.pvariance(nums))
# Sample standard deviation of data
print("Sample standard deviation of data (stdev)")
print(statistics.stdev(nums))
# Population variance of data
print("Sample variance of data (variance)")
print(statistics.variance(nums))

