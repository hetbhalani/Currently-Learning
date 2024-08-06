def main():
    try:
        a = int(input("enter: "))
        return

    except Exception as e:
        print(e)
        return

    finally:
        print("This is finally block...")

main()
print("Over")