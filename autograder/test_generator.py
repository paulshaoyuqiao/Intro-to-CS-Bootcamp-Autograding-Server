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
        total_output = []
        actual_total_scores, total_scores, method_count = 0, 0, 0
        for test_method in test_info.keys():
            total_test_cases = test_info[test_method]
            method_path = '{}/{}_test.rb'.format(test_path, test_method)
            test_class = '{}Test'.format(test_method[0].upper() + test_method[1:])
            for i in range(1, total_test_cases + 1):
                test_method_i = '{}.test_{}_{}'.format(test_class, test_method, i)
                test_output = check_output(
                    ['ruby', '-r', method_path, '-e', test_method_i]
                )
                decoded_raw_output = test_output.decode('utf-8')
                output_dict = TestRunner.parse_output(decoded_raw_output, i)
                actual_total_scores += int(output_dict['actual_score'])
                total_scores += int(output_dict['total_score'])
                total_output.append(output_dict)
            method_count += 1
        test_summary = {
            'total_full_score': total_scores,
            'actual_full_score': actual_total_scores,
            'total_test_cases': total_test_cases,
            'method_count': method_count
        }
        return test_summary, total_output

    @staticmethod
    def parse_output(raw_string, index=1):
        output_dict = {}
        output_arr = raw_string.split("<=>")
        method_name = output_arr[0].strip()
        test_name = "test_{}_{}".format(method_name, index)
        method_args = output_arr[1].replace("&", ", ").strip()
        output_dict['test_name'] = test_name
        output_dict['test_input'] = "{}({})".format(method_name, method_args)
        output_dict['expected_output'] = output_arr[2].strip()
        output_dict['actual_output'] = output_arr[3].strip()
        output_dict['actual_score'] = output_arr[4].strip()
        output_dict['total_score'] = output_arr[5].strip()
        return output_dict
