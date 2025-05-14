# - Flask : 웹 서버 생성
# - render_template : HTML 템플릿 랜더링
# - request : 사용자 요청 처리
# - redirect ,url_for : 페이지 이동 및 URL 생성
from flask import Flask, render_template, request, redirect, url_for

# Flask 객체 생성. Flask 앱의 시작점. 이 객체를 통해 모든 요청과 응답을 관리.
app = Flask(__name__)

# 할 일을 저장할 리스트 (임시 저장소, 재시작 시 초기화됨)
tasks = []

# 메인 페이지(/)에 접속 시 호출되는 함수.
@app.route('/')
def index():
    print(tasks)
    # index.html을 렌더링하고 tasks 리스트를 전달
    return render_template('index.html', tasks=tasks)


# 폼에서 "추가" 버튼을 눌렀을 때 호출
@app.route('/add', methods=['POST'])
def add_task():
    # 폼에서 입력된 'task' 데이터를 가져옴
    task = request.form['task']
    if task:  # 빈 입력 방지
        tasks.append(task)
    # 메인 페이지로 리디렉션
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    if 0 <= task_id < len(tasks):
        print(f"삭제됨: {tasks[task_id]}")  # 삭제된 항목 출력
        tasks.pop(task_id)
    return redirect(url_for('index'))


# HTML과 CSS가 필요
if __name__ == '__main__':
    app.run(debug=True) # debug=True는 코드 변경 시 자동 재시작하고 에러 메시지를 자세히 표시
