
# เขียนโปรแกรมหา index ของตัวเลขที่มีค่ามากที่สุดใน Array ด้วยภาษา python เช่น [1,2,1,3,5,6,4] 
# ลำดับที่มีค่ามากที่สุด คือ index = 5 โดยไม่ให้ใช้ฟังก์ชั่นที่มีอยู่แล้ว ให้ใช้แค่ลูปกับการเช็คเงื่อนไข

def main():
    arr = [1, 2, 1, 3, 5, 6, 4]
    max_num_index = 0
    current_value = 0
    for i in range(len(arr)):
        if (arr[i] > current_value):
            current_value = arr[i]
            max_num_index = i

    print(f"Index with maximum number in Array is: {max_num_index}")

if __name__ == "__main__":
    main()