import time

# Số lượng phần tử trong mảng
n = 2*10**6

# Bắt đầu đo thời gian
start_time = time.time()

# Tạo mảng bool với n phần tử
bool_array = [False] * n

# Kết thúc đo thời gian
end_time = time.time()

# Tính thời gian thực thi
execution_time = end_time - start_time

print(f"Thời gian để tạo mảng bool {n} phần tử: {execution_time} giây")
