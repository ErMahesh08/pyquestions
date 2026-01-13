data = {
    "employees": [
        [
            "id", 101,
            "name", "Alice",
            "skills", ["Python", "SQL", "GCP"],
            "projects", [
                {"project_id": "P1", "status": "Completed"},
                {"project_id": "P2", "status": "Ongoing"}
            ],
            ["id", 102,
            "name", "Bob",
            "skills", ["Python", "SQL", "GCP"],
            "projects", [
                {"project_id": "P1", "status": "Completed"},
                {"project_id": "P2", "status": "Ongoing"}]
            ]
        ]
    ]
}
# print(len(data))
# print(data.values())
list1 = list(data.values())
# print(len(list1))
# # print(list1)
list2 = list1[0]
# print(len(list2))
# print(list2)
list3 = list2[0]
# print(len(list3))
# # print(list3)
list4 = list3[8]
# # print(list4)
list5 = list3[8]
# # print(len(list5))
# # print(list5)
print(list5[:2])
print(list5[2:4])
#  Want to print below output
#  "id", 102,
#  "name", "Bob"
