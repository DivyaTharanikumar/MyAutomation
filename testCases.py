# we can add and maintain list of test cases here so that we donot miss some cases while writing automation code
# and test analysts can handle this more efficiently
# we can obtain test cases from test management tools, like: http://www.inflectra.com/SpiraTest/Integrations/Unit-Test-Frameworks.aspx
# We can also record the result of test cases to test management tool

# for maintainability, we can separate web test cases by page name but I just listed every case in same array

def test_cases(number):
    return testCases[number]


testCases = [
    # [severity, description]
    ['Blocker', 'when user goes to main page, page should be loaded'],
    ['Blocker', 'In Main page, when user hits search "Lenovo" button, he should see results for Nexus 5'],
    ['Blocker', 'In Main page, when user clicks "Sign up" button, he should see Sign up Page'],
    ['Blocker', 'In Main page, when user clicks "Sign in" button, he should see Sign in Page'],
    ['Blocker', 'In Login Page, when user tries to login with a valid user id, he should see Home Page'],
    ['Blocker', 'In Login Page, when user tries to login with a in-valid user id, he should see Error Message'],
]
