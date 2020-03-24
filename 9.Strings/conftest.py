import pathlib


# 3 test cases do fail (lines 1357, 4062, 4556) because given test data is invalid. Shame otus.ru :(
def pytest_generate_tests(metafunc):
    config = pathlib.Path(metafunc.module.__file__).with_name(
        'string_matching_test_cases_31272_751472-57251-751472.tsv')
    with config.open() as tsv_file:
        lines = tsv_file.readlines()
        test_data = []
        for line in lines:
            test_case = line.strip().split('\t')
            if len(test_case) == 2:
                test_data.append((test_case[0], test_case[1], ()))
            elif len(test_case) == 3:
                test_data.append((test_case[0], test_case[1], tuple(int(x) for x in test_case[2].split(' '))))
        if 'text' in metafunc.fixturenames:
            metafunc.parametrize(('text', 'pattern', 'match_locations'), test_data)
