def product_of_array_except_self(nums):
    n = len(nums)
    prefix = 1
    postfix = 1
    result = [1] * n

    # Computing prefix.
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]

    # Computing postfix.
    for i in range(n - 1, -1, -1):
        result[i] *= postfix
        postfix *= nums[i]

    return result


if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    print(product_of_array_except_self(nums))
