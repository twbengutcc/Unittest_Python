จาก Code ข้างต้นเป็นการทดสอบการใช้ Stack และการใช้งาน Unittest ใน Python
ขั้นตอนการประมวดผลและกลไกมีดังนี้
Stack เป็น Data Structure ประเภทนึงที่มีลักษณะเป็นชั้น ๆ หรือกล่องซ้อนกัน โดยมีหลักการอยู่ว่า เราจะเก็บอะไรก็ได้ แต่เวลาเราจะเข้าถึงข้อมูล เราไม่สามารถเข้าถึงเป็น Index ได้ 
เราจะเข้าถึงได้เฉพาะข้อมูลที่เราเติมอันล่าสุด โดยจะมี 2 Operation เรียกว่า Push และ Pop

Push คือการเอา Data เข้าไปวางไว้ใน Stack
Pop คือการเอาข้อมูลที่พึ่ง Push ไปล่าสุดออกมาออกมา

การ Code เป็นการสร้างฟังก์ชัน bracket_check และใช้คลาส Stack เพื่อตรวจสอบว่าวงเล็บในข้อความที่กำหนดถูกปิดทุกครั้งหรือไม่ โดยใช้ Code ดังนี้ 

from Stack import Stack


# input: str
# output: ib_error : boolean
# output: location : int

def bracket_check(str):
    is_error = False
    location = []
    stack = Stack()

    for i in range(len(str)):
        s = str[i]
        if s == '(' or s == '[' or s == '{':
            stack.push((s, i))
        elif s == ')' or s == ']' or s == '}':
            if not stack.isEmpty():
                p, pos = stack.pop()
            else:
                is_error = True
                location.append(i)
                continue

            if not ((p == '(') and (s == ')') or ((p == '[') and (s == ']')) or ((p == '{') and s == '}')):
                is_error = True
                location.append(i)
                break

    while not stack.isEmpty():
        _, pos = stack.pop()
        location.append(pos)

    if location:
        is_error = True

    return is_error, location


test_string = '[{(Hello)}]'
isError, locations = bracket_check(test_string)
print(f'error: {isError}')
print('location:', locations)


โดยมีการทำ Unittest ทั้งหมด 5 Test Cases ดังนี้

test_no_error ตรวจสอบคำว่า '[{(Hello)}]'
test_error_1 ตรวจสอบคำว่า '[{(Hello})]'
test_error_2 ตรวจสอบคำว่า '[{(Hello'
test_error_3 ตรวจสอบคำว่า 'Hello)('
test_error_4 ตรวจสอบคำว่า '{}{'

พร้อมใช้คำสั่ง assertEqual เพื่อตรวจสอบผลลัพธ์

ผลลัพธ์ออกมาหลังจากที่ Run Unittest พบว่า test_error_4 นั้น run ไม่ผ่านเนื่องจากมีการตรวจสอบที่ต้องการให้ location เป็น [2] อ้างอิง Code การตรวจสอบ

    def test_error_4(self):
        test_string = '{}{'
        isError, location = bracket_check(test_string)
        self.assertEqual(isError, True)
        self.assertEqual(location, [2])

ดังนั้นจึงได้ลองแก้ไข Code ในส่วนของ bracket_check ให้ครอบคลุมสิ่งที่ต้องการเพิ่มเติมโดย
1.เพิ่มการเก็บตำแหน่งของวงเล็บลงใน stack ด้วย การเก็บ (s, i) ที่ i คือตำแหน่งของวงเล็บ
2.การตรวจสอบ stack ที่เหลือ เพิ่ม Loop, while เพื่อตรวจสอบ stack ที่เหลือหลังจาก Loop หลักเสร็จ และเพิ่มตำแหน่งของวงเล็บเข้าไปใน location
3.การตรวจสอบ location แทนที่จะตรวจสอบ not stack.isEmpty() จะตรวจสอบ location โดยให้ is_error = True เมื่อ location ไม่ว่าง

หลังจากแก้ไขแล้วจะได้ Code ดังนี้

def bracket_check(str):
    is_error = False
    location = []
    stack = Stack()

    for i in range(len(str)):
        s = str[i]
        if s == '(' or s == '[' or s == '{':
            stack.push((s, i))
        elif s == ')' or s == ']' or s == '}':
            if not stack.isEmpty():
                p, pos = stack.pop()
            else:
                is_error = True
                location.append(i)
                continue

            if not ((p == '(') and (s == ')') or ((p == '[') and (s == ']')) or ((p == '{') and s == '}')):
                is_error = True
                location.append(i)
                break

    while not stack.isEmpty():
        _, pos = stack.pop()
        location.append(pos)

    if location:
        is_error = True

    return is_error, location

ผลลัพธ์ออกมาหลังจากที่ Run Unittest พบว่าผ่านทุกการทดสอบ

