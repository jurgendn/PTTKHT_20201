# Docs

## Cài đặt Django

Docs này viết cho người dùng `Windows`

### Cài Python

[Links](https://www.python.org/downloads/windows/)

### Virtual Environment

Có thể cài trực tiếp lên thư mục gốc, tuy nhiên như thế thì dễ loạn

Ông nào thích thì cũng chiều, có thể bỏ qua bước này

#### Virtual Environment

> Là môi trường ảo, độc lập với các môi trường ảo khác và môi trường gốc. Các packages, modules cài đặt trong virtual environment không ảnh hưởng đến các môi trường khác.

`Command trong shell`

```bash
pip3 install virtualenv
```

Để tạo một venv mới, thực hiện câu lệnh sau tại thư mục mong muốn. Ví dụ project đặt ở `D:\\django_project\`, mở một shell trong thư mục trên và chạy câu lệnh sau:

```powershell
virtualenv `env_name`
```

'env_name' là tên cho environment, có thể đặt như nào cũng được, tùy vào mục đích. Trong bài này, giả sử đặt là `d_project`.

Sau khi đã khởi tạo một venv, để sử dụng venv này thay cho env gốc, chạy câu lệnh sau:

```shell
\pathto\env\Scripts\activate
```

Ví dụ:

```shell
D:\\django_project\d_project\Scritps\activate
```

#### Django

Django là gì thì trên web đã tả rõ.

Cài Django trên venv sau khi đã activate venv như trên python gốc:

```shell
pip install django
```

## Quy tắc viết code

### Code Layout

1. **Indentation**
   Dùng tab (4 spaces) để phân định các cấp của lệnh.

   ```python
   # Correct:
   
   # Aligned with opening delimiter.
   foo = long_function_name(var_one, var_two,
                            var_three, var_four)
   
   # Add 4 spaces (an extra level of indentation) to distinguish arguments from the rest.
   def long_function_name(
           var_one, var_two, var_three,
           var_four):
       print(var_one)
   
   # Hanging indents should add a level.
   foo = long_function_name(
       var_one, var_two,
       var_three, var_four)
   ```

   ```python
   # Wrong:
   
   # Arguments on first line forbidden when not using vertical alignment.
   foo = long_function_name(var_one, var_two,
       var_three, var_four)
   
   # Further indentation required as indentation is not distinguishable.
   def long_function_name(
       var_one, var_two, var_three,
       var_four):
       print(var_one)
   ```

   2. **Tabs hay Spaces**
      Theo autopep8, spaces thường được sử dụng hơn, tuy nhiên ở đây nên thống nhất dùng tabs cho nhanh.

   3. **Giới hạn độ dài**
      Mỗi dòng nên được giới hạn ở 79 kí tự. Đặt trong setting của editor. Các editor có thể khác nhau.

   4. **Xuống dòng trước toán tử toán học**
      Đối với biểu thức dài, xuống dòng trước khi đặt toán tử . Minh họa như sau:

      ```python
      # Wrong:
      # operators sit far away from their operands
      income = (gross_wages +
                taxable_interest +
                (dividends - qualified_dividends) -
                ira_deduction -
                student_loan_interest)
      ```

      Nên được viết như sau:

      ```python
      # Correct:
      # easy to match operators with operands
      income = (gross_wages
                + taxable_interest
                + (dividends - qualified_dividends)
                - ira_deduction
                - student_loan_interest)
      ```

   5. **Dòng trắng**

      - Giữa các phương thức (`method`) cách nhau bởi ***một dòng trống***

      - Giữa các lớp (`class`) và phương thức (`method`) cách nhau bởi ***hai dòng trống***

      - Các khối code (`block`) cách nhau riêng biệt bằng ***một dòng trống***

        ***Ví dụ:***

        ```python
        class PoissonHiddenMarkov:
            
            
            def train_by_baum_welch(self, data):
                # Statement
                
        	def get_hidden_states(self, data):
                #Statement
                
        class MarkovProcess:
            
            
            def get_generated_matrix(self):
                # Statements
           
        	def get_stationary_distribution(self):
                # Statement
        ```

   6. **Import**

      1. Các mỗi một module nên được viết trên một dòng khác nhau

         ```python
         # Correct:
         import os
         import sys
         ```

         ```pythonpython]
         # Wrong:
         import sys, os
         ```

      2. Đối với các submodules trong một module, có thể được import chung trong một dòng

         ```python
         # Correct:
         from subprocess import Popen, PIPE
         ```

      3. Import ***luôn luôn*** đặt ở đầu file, ngay sau module comments và docstrings.

      4. Import nên được chia thành 3 phần riêng biệt

         - Thư viện chuẩn
         - Thư viện của bên thứ ba
         - Các module tự viết, local modules

      5. **Quotes**
         Các string được đặt trong ```"string"```

### Đặt tên

#### Class

> Các `class` nên được viết hoa mỗi chữ đầu của một từ (`word`), viết liền.

##### Ví dụ

```python
# Correct

class CapWords:

    
class PoissonHiddenMarkovModel:
    
    
# Wrong

class cap_word:
    
    
class Poissonhiddenmarkovmodel:
```

#### Biến và hàm

> Viết thường, các từ được phân tách bởi dấu _

Tên hàm, biến có ý nghĩa, không đặt những tên không chỉ mục đích, ý nghĩa của hàm, biết.

```python
# Correct

MAX_ITE = 100	# no more than 100 loops
ite				# current iteration


# Wrong

k = 100			# maximum iteration
i				# current iteration
```

Trong trường hợp nhiều biến, bên cạnh việc đặt tên có ý nghĩa, lập một bảng ở ngoài, định dạng markdown ánh xạ mỗi biến với hàm tương ứng trong chương trình

#### Arguments của hàm và method

1. Đối với instance method trong class, luôn dùng `self` là argument đầu tiên

   > Hầu hết rơi vào trường hợp này

2. Đối với class method, dùng `cls` là argument đầu tiên.

#### Tên method và instance variables

1. Sử dụng tên method như đã quy ước với tên hàm, biến.
2. Dùng **một** dấu _ ở trước tên các hàm, các biến private.

#### Hằng số

Hằng số được VIẾT_HOA_TOÀN_BỘ và phân cách bởi dấu _

---

> Các quy tắc khác sẽ được bổ sung trong quá trình thực hiện

### Quy ước về đặt tên

1. Hàm dùng để lấy thông tin, bắt đầu bằng `get`. Ví dụ

   ```python
   def get_user_by_name(name):
       # Statements
   ```

2. Hàm dùng để kiểm tra mệnh đề nào đó, bắt đầu bằng `is`. Ví dụ:

   ```python
   def is_active(user):
       # Statements
   ```

3. Hàm dùng để đặt trạng thái, thông số cho đối tượng, bắt đầu bằng `set`. Ví dụ:

   ``` python
   def set_active_status(user):
       # Statements
   ```

4. Hàm dùng để khởi tạo một cái gì đó, bắt đầu bằng `create`. Ví dụ:

   ```python
   def create_connection_to_db():
       # Statements
   ```

5. Hàm để xóa cái gì đó, bắt đầu bằng `remove`. Ví dụ:

   ```python
   def remove_item_from_cart(item, cart):
       # Statements
   ```

> Tạm thời có 5 trường hợp cơ bản, nếu có phát sinh tình huống vui lòng thông báo để bổ sung kịp thời

---

## Một số hướng dẫn cơ bản về Django và cách sử dụng Template

### Django

[Documentation](https://docs.djangoproject.com/en/3.1/) của Django hướng dẫn rất đầy đủ và chi tiết, ở đây không nhắc lại.

### Templates

> Django có thể sử dụng cả templates tích hợp hoặc Jinja2, ở đây chọn Jinja2 vì có vẻ như có documentation tốt hơn

---

## Jinja2

Concept chung có thể được mô tả qua hình sau:



### Template file

Ví dụ, file `base.html` với cấu trúc như sau:

```html
<!doctype html>
<title>{% block title %}{% endblock %} - Django</title>
<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
<nav>
  <h1>Django</h1>
  <ul>
    {% if g.user %}
      <li><span>{{ g.user['username'] }}</span>
      <li><a href="{{ url_for('auth.logout') }}">Log Out</a>
    {% else %}
      <li><a href="{{ url_for('auth.register') }}">Register</a>
      <li><a href="{{ url_for('auth.login') }}">Log In</a>
    {% endif %}
  </ul>
</nav>
<section class="content">
  <header>
    {% block header %}{% endblock %}
  </header>
  {% for message in get_flashed_messages() %}
    <div class="flash">{{ message }}</div>
  {% endfor %}
  {% block content %}{% endblock %}
</section>
```

Trong đoạn code trên, chú ý vào cấu trúc của file, ta thấy:

1. `<!doctype>`  là phần định cấu trúc của html, nói chung là file nào cũng phải có cái này

2. `<title></title>`: Phần tiêu đề của trang web

3. Phần nằm giữa `<nav></nav>` là phần navigation bar. Trong file trên, phần navigation bar gồm có các elements sau:

   - Log Out: Đăng xuất
   - Register: Đăng kí
   - Log In: Đăng nhập

   Nói chung là tùy vào điều kiện mà các elements trên navbar có thể khác nhau.

4. Phần nằm giữa `<section></section>` là phần nội dung của trang. Trong phần này, có 2 phần lớn

   - `<header></header>` là phần header của page. Cụ thể hơn, `header` là gì thì nên search google, giải thích ở đây không hợp lí
   - Phần còn lại là phần nội dung.

#### Các block

##### Chức năng

Nhìn vào đoạn chương trình mẫu cho file `base.html`, ta thấy có các đoạn `{% block title %} {% endblock %} ,{% block header %} {% content %} ,...` Nói chung đây là phần rất quan trọng. Nội dung của từng block sẽ được define trong các file template khác. 

Các page khi load sẽ được load theo thứ tự sau:

1. Chọn một template cơ bản, ví dụ như file `base.html` ở trên.
2. Từng phần một sẽ được load vào vị trí tương ứng, xác định bởi các đoạn `{% block %}{% endblock %}` ở trên.
3. Nội dung của từng block được xử lí bên ngoài.

Nói chung, ai đã từng tạo block với Jekyll thì sẽ thấy khá là quen thuộc, bởi cách thức tạo các template khá tương đồng, bên cạnh đó thì cú pháp của Jinja2 và Liquid cũng khá giống nhau.

Ví dụ, với file `base.html` đã viết ở trên, khi muốn load page `register.html`, ta làm như sau:

```html
{% extends 'base.html' %}

{% block header %}
  <h1>{% block title %}Register{% endblock %}</h1>
{% endblock %}

{% block content %}
  <form method="post">
    <label for="username">Username</label>
    <input name="username" id="username" required>
    <label for="password">Password</label>
    <input type="password" name="password" id="password" required>
    <input type="submit" value="Register">
  </form>
{% endblock %}
```



- Dòng đầu tiên `{% extend base.html %}` cho biết trang `register.html` sẽ sử dụng file cơ sở là `base.html`.

- ```html
  {% block header %}
    <h1>{% block title %}Register{% endblock %}</h1>
  {% endblock %}
  ```

  Đoạn code này xác định các thành phần `header` và `title`. Nội dung của phần này sẽ được chèn vào vị trí tương ứng trong file `base.html`.

- ```html
  {% block content %}
    <form method="post">
      <label for="username">Username</label>
      <input name="username" id="username" required>
      <label for="password">Password</label>
      <input type="password" name="password" id="password" required>
      <input type="submit" value="Register">
    </form>
  {% endblock %}
  ```

  Đoạn này là nội dung cho phần `content`, cách thức chèn tương tự như trên, tức là chèn vào vị trí `content` trong file `base.html`.

Đến cuối cùng, chương trình hoàn chỉnh cho page `register.html ` sẽ được render như sau:

```html
<!doctype html>
<title>Register - Django</title>
<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
<nav>
  <h1>Flaskr</h1>
  <ul>
    {% if g.user %}
      <li><span>{{ g.user['username'] }}</span>
      <li><a href="{{ url_for('auth.logout') }}">Log Out</a>
    {% else %}
      <li><a href="{{ url_for('auth.register') }}">Register</a>
      <li><a href="{{ url_for('auth.login') }}">Log In</a>
    {% endif %}
  </ul>
</nav>
<section class="content">
  <header>
    <h1>Register</h1>
  </header>
  {% for message in get_flashed_messages() %}
    <div class="flash">{{ message }}</div>
  {% endfor %}
  <form method="post">
    <label for="username">Username</label>
    <input name="username" id="username" required>
    <label for="password">Password</label>
    <input type="password" name="password" id="password" required>
    <input type="submit" value="Register">
  </form>
</section>
```



> Lưu ý là các hàm, các biến sử dụng ở trên được giả định là đã tồn tại trong chương trình.

> Nói chung là đến đây thì biết đến thế, chứ tiếp theo làm như nào với đống static file thì tôi cũng chưa rõ lmao

## Dùng Git

Git là một phần mềm quản lí phiên bản (distributed version control system). 

