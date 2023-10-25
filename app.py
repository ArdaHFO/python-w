from flask import Flask, render_template, request
import random
from views import views

app = Flask(__name__)
app.register_blueprint(views, url_prefix="/")

@app.route('/', methods=['GET', 'POST'])
def random_team_generator():
    if request.method == 'POST':
        members = request.form.get('members')
        if members:
            members = members.split(',')
            random.shuffle(members)

            num_teams = int(request.form.get('num_teams'))
            teams = {f'Team {i}': [] for i in range(1, num_teams + 1)}

            for i, member in enumerate(members):
                team = f'Team {i % num_teams + 1}'
                teams[team].append(member)

            return render_template('teams.html', teams=teams)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
    app.run()