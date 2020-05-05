

def test_cases(number):
    return testCases[number]


testCases = [
    # [severity, description]
    ['Blocker', 'when user goes to main page, page should be loaded'],
    ['Blocker', 'In Main page, when user hits search "Lenovo" button, he should see results for lenovo'],
    ['Blocker', 'In Main page, when user clicks "Sign up" button, he should see Sign up Page'],
    ['Blocker', 'In Main page, when user clicks "Sign in" button, he should see Sign in Page'],
    ['Blocker', 'In Login Page, when user tries to login with a valid user id, he should see Home Page'],
    ['Blocker', 'In Login Page, when user tries to login with a in-valid user id, he should see Error Message'],
]
