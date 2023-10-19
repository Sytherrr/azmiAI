from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from performance_analysis.forms import StudentForm
from performance_analysis.models import Student
from performance_analysis.analysis import perform_analysis
from plotly.offline import plot
import plotly.graph_objs as go

# User_Authentication
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

@login_required
def input_form_view(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()
            return redirect('results')
    else:
        form = StudentForm()
    return render(request, 'input_form.html', {'form': form})

def data_submissions_view(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()
            analysis_results = perform_analysis(student)
            return redirect('results')
    else:
        form = StudentForm()
    return render(request, 'data_submission.html', {'form': form})

# Authentication
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('input_form')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('input_form')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

def analyze_student_performance(request, student_id):
    student = Student.objects.get(id=student_id)
    analysis_results = perform_analysis(student)
    return render(request, 'analysis_result.html', {'analysis_results': analysis_results })

@login_required
def results_view(request):
    analysis_results = {
        'model_name': 'Linear Regression',
        'gpa': 3.5,
        'attendance': 'Always',
        'prediction': 85,
    }

    chart = go.Bar(
        x=['GPA', 'Attendance'],
        y=[analysis_results['gpa'], analysis_results['prediction']],
        text=['GPA', 'Prediction'],
        marker=dict(color=['blue', 'green'])
    )

    chart_layout = go.Layout(
        title='Student Performance Analysis',
    )

    chart_fig = go.Figure(data=[chart], layout=chart_layout)
    chart_div = plot(chart_fig, output_type='div', include_plotlyjs=False)

    return render(request, 'results.html', {'analysis_results': analysis_results, 'chart_div': chart_div})
