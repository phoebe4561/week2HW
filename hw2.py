def calculate(min, max):
    sum = 0
    for x in range(min, max+1):
        sum = sum+x
    print(sum)


calculate(1, 3)
calculate(4, 8)


def avg(data):
    num = data['count']
    sal = data['employees']
    total = 0
    for i in sal:
        sal = i['salary']
        total += sal
    avg = total/num

    print(avg)


avg({
    "count": 3,
    "employees": [
        {"name": "John", "salary": 30000},
        {"name": "Bob", "salary": 60000},
        {"name": "Jenny", "salary": 50000}
    ]
})


def maxProduct(nums):
    m = -999999999
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            k = nums[i]*nums[j]
            if k > m:
                m = k
    print(m)


maxProduct([5, 20, 2, 6])
maxProduct([10, -20, 0, 3])


def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i]+nums[j] == target:
                return [i, j]


result = twoSum([2, 11, 7, 15], 9)
print(result)
