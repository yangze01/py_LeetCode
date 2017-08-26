#coding=utf8
class my_stack(object):
    def __init__(self, value):
        self.value = value
        # 前驱
        self.before = None
        # 后继
        self.behind = None

    def __str__(self):
        return str(self.value)
def top(stack):
    if isinstance(stack, my_stack):
        if stack.behind is not None:
            return top(stack.behind)
        else:
            return stack

def push(stack, ele):
    push_ele = my_stack(ele)
    if isinstance(stack, my_stack):
        stack_top = top(stack)
        push_ele.before = stack_top
        push_ele.before.behind = push_ele
    else:
        raise Exception('无法存入栈')

def pop(stack):
    if isinstance(stack, my_stack):
        stack_top = top(stack)
        if stack_top.before is not None:
            stack_top.before.behind = None
            stack_top.behind = None
            return stack_top
        else:
            print("到达栈顶")


if __name__ == "__main__":
    test_stack = my_stack(0)
    for i in range(0, 10):
        push(test_stack, i)

    for i in range(0, 11):
        print(pop(test_stack))
