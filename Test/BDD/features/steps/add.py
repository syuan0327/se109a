from behave import given, when, then
use_step_matcher('re')

@given('I have two integers "first" and "second"')
def step_impl(context):
    context.first = 5
    context.second = 10
@when('I add the two numbers')
def step_impl(context):
    context.sum = context.first + context.second
@then('I get the sum')
def step_impl(context):
    print(context.sum)