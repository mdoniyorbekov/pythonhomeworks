def enrollment_stats(universities):
    enrollments = [uni[1] for uni in universities]
    tuitions = [uni[2] for uni in universities]
    return enrollments, tuitions
def mean(lst):
    return sum(lst)/len(lst) if lst else 0
def median(lst):
    sorted_lst=sorted(lst)
    n = len(sorted_lst)
    mid = n//2
    if n%2 == 0:
        return (sorted_lst[mid-1] + sorted_lst[mid])/2
    else:
        return sorted_lst[mid]
universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]
enrollments, tuitions = enrollment_stats(universities)
total_students = sum(enrollments)
total_tuition = sum(tuitions)
student_mean = mean(enrollments)
student_median = median(enrollments)
tuition_mean = mean(tuitions)
tuition_median = median(tuitions)

print("******************************")
print(f"Total students: {total_students:,}")
print(f"Total tuition: {total_tuition:,}\n")
print(f"Student mean: {student_mean:,.2}")
print(f"Student median: {student_median:,}\n")
print(f"Tuition mean: {tuition_mean:,.2}")
print(f"Tuition median: {tuition_median:,}")
print("******************************")