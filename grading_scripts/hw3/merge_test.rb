require_relative "merge.rb"
class MergeTest
    @@method = "merge"
    # output follows the order of "method_name <=> inputs <=> expected <=> output <=> score"
    def self.format_and_flush(expected, actual, inputs)
        total_score = 1
        actual_score = 0
        if expected == actual
            actual_score += 1
        end
        puts "#{@@method} <=> #{inputs} <=> #{expected} <=> #{actual} <=> #{actual_score} <=> #{total_score}"
    end

    def self.test_merge_1
        inp_1 = [1, 3]
        inp_2 = [2, 4]
        oup = merge(inp_1, inp_2)
        expected = [1, 2, 3, 4]
        MergeTest.format_and_flush(expected, oup, "#{inp_1}&#{inp_2}")
    end

    def self.test_merge_2
        inp_1 = [1, 2]
        inp_2 = [2, 3, 4]
        oup = merge(inp_1, inp_2)
        expected = [1, 2, 2, 3, 4]
        MergeTest.format_and_flush(expected, oup, "#{inp_1}&#{inp_2}")
    end

    def self.test_merge_3
        inp_1 = [1, 2]
        inp_2 = []
        oup = merge(inp_1, inp_2)
        expected = [1, 2]
        MergeTest.format_and_flush(expected, oup, "#{inp_1}&#{inp_2}")
    end

    def self.test_merge_4
        inp_1 = []
        inp_2 = []
        oup = merge(inp_1, inp_2)
        expected = []
        MergeTest.format_and_flush(expected, oup, "#{inp_1}&#{inp_2}")
    end

    def self.test_merge_5
        inp_1 = [1, 3, 4, 5, 9]
        inp_2 = [2, 4, 6, 7, 8]
        oup = merge(inp_1, inp_2)
        expected = [1, 2, 3, 4, 4, 5, 6, 7, 8, 9]
        MergeTest.format_and_flush(expected, oup, "#{inp_1}&#{inp_2}")
    end

    def self.test_merge_6
        inp_1 = [1, 3, 4, 5, 9, 10]
        inp_2 = [2, 4, 6, 7, 8]
        oup = merge(inp_1, inp_2)
        expected = [1, 2, 3, 4, 4, 5, 6, 7, 8, 9, 10]
        MergeTest.format_and_flush(expected, oup, "#{inp_1}&#{inp_2}")
    end

    def self.test_merge_7
        inp_1 = [1, 3, 4, 5, 9]
        inp_2 = [2, 4, 6, 7, 8, 10]
        oup = merge(inp_1, inp_2)
        expected = [1, 2, 3, 4, 4, 5, 6, 7, 8, 9, 10]
        MergeTest.format_and_flush(expected, oup, "#{inp_1}&#{inp_2}")
    end

    def self.test_merge_8
        inp_1 = [1, 3, 4, 5, 9, 10]
        inp_2 = [2, 4, 6, 7, 8, 10]
        oup = merge(inp_1, inp_2)
        expected = [1, 2, 3, 4, 4, 5, 6, 7, 8, 9, 10, 10]
        MergeTest.format_and_flush(expected, oup, "#{inp_1}&#{inp_2}")
    end
end