courses=["Ms Office","Css & Html","Javascript","Sql","Php","Flutter",".Net","Python","C#","Laravel"]
print(courses)
print(courses[6])
print(courses[-3])
print(courses[-1])
print(courses[2:6])
print(f"Total courses length is : {len(courses)}")

courses.append("Python")
print(f"After append {courses}")

courses.append("Hadoop")
print(f"After append {courses}")

courses.insert(6,"PWD")
print(f"After insert {courses}")

courses.insert(9,"Data Analytics")
print(f"After insert {courses}")

print(f"Total length of courses is : {len(courses)}")

more_courses=["mongodb","flutter","Nodejs","VueJs"]

courses.extend(more_courses)
print(f"After extend : {courses}")

print(f"Total length of courses is : {len(courses)}")

courses.remove("Css & Html")
print(f"After remove {courses}")

courses.pop()
print(f"After pop {courses}")

print(f"Total length of courses is : {len(courses)}")

courses.sort()
print(f"Ascending order : {courses}")

courses.sort(reverse=True)
print(f"Descending order is : {courses}")

more_courses_add=["Urdu","IOT","Networking"]

courses.extend(more_courses_add)
print(f"After extend : {courses}")

print(f"Total length of courses is : {len(courses)}")

courses.clear()
print(f"After clearing list {courses}")

print(f"Total length of courses is : {len(courses)}")