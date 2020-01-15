from subprocess import check_output

tests_by_week = {
    'hw3': {'merge': 8}
}

assignment_by_method = {
    'merge': 'hw3'
}

class TestRunner:
    @staticmethod
    def run_tests(assignment):
        test_path = './grading_scripts/{}'.format(assignment)
        test_info = tests_by_week[assignment]
        total_output = ''
        for test_method in test_info.keys():
            total_test_cases = test_info[test_method]
            method_path = '{}/{}_test.rb'.format(test_path, test_method)
            test_class = '{}Test'.format(test_method[0].upper() + test_method[1:])
            for i in range(1, total_test_cases + 1):
                test_method_i = '{}.test_{}_{}'.format(test_class, test_method, i)
                test_output = check_output(
                    ['ruby', '-r', method_path, '-e', test_method_i]
                )
                total_output += test_output.decode('utf-8')
        return total_output
