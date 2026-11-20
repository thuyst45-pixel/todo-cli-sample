"""Ứng dụng quản lý công việc (To-Do) đơn giản chạy trên dòng lệnh."""
import json
from pathlib import Path

DATA_FILE = Path("tasks.json")


def load_tasks():
    """Đọc danh sách công việc từ file JSON."""
    if DATA_FILE.exists():
        return json.loads(DATA_FILE.read_text(encoding="utf-8"))
    return []


def save_tasks(tasks):
    """Lưu danh sách công việc vào file JSON."""
    DATA_FILE.write_text(
        json.dumps(tasks, ensure_ascii=False, indent=2), encoding="utf-8"
    )


def show_tasks(tasks):
    if not tasks:
        print("Chưa có công việc nào.")
        return
    for i, task in enumerate(tasks, start=1):
        mark = "x" if task["done"] else " "
        print(f"{i}. [{mark}] {task['title']}")


def ask_index(tasks, action):
    """Hỏi người dùng số thứ tự công việc, trả về chỉ số hợp lệ hoặc None."""
    show_tasks(tasks)
    if not tasks:
        return None
    try:
        number = int(input(f"Nhập số thứ tự công việc cần {action}: "))
    except ValueError:
        print("Vui lòng nhập một số.")
        return None
    if 1 <= number <= len(tasks):
        return number - 1
    print("Số thứ tự không hợp lệ.")
    return None


def main():
    tasks = load_tasks()
    while True:
        print("\n=== TO-DO LIST ===")
        print("1. Xem danh sách")
        print("2. Thêm công việc")
        print("3. Đánh dấu hoàn thành")
        print("4. Xóa công việc")
        print("0. Thoát")
        choice = input("Chọn chức năng: ").strip()

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            title = input("Nhập tên công việc: ").strip()
            if title:
                tasks.append({"title": title, "done": False})
                save_tasks(tasks)
                print("Đã thêm công việc.")
            else:
                print("Tên công việc không được để trống.")
        elif choice == "3":
            index = ask_index(tasks, "hoàn thành")
            if index is not None:
                tasks[index]["done"] = True
                save_tasks(tasks)
                print("Đã đánh dấu hoàn thành.")
        elif choice == "4":
            index = ask_index(tasks, "xóa")
            if index is not None:
                removed = tasks.pop(index)
                save_tasks(tasks)
                print(f"Đã xóa: {removed['title']}")
        elif choice == "0":
            print("Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng thử lại.")


if __name__ == "__main__":
    main()
