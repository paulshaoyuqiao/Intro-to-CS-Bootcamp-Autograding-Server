require_relative "merge.rb"
class MergeTest
    def self.test_merge_1
        inp_1 = [1, 3]
        inp_2 = [2, 4]
        oup = merge(inp_1, inp_2)
        expected = [1, 2, 3, 4]
        if expected == oup
            puts 'matched'
        else
            puts "#{oup}"
        end
    end

    def self.test_merge_2
        inp_1 = [1, 2]
        inp_2 = [2, 3, 4]
        oup = merge(inp_1, inp_2)
        expected = [1, 2, 2, 3, 4]
        if expected == oup
            puts 'matched'
        else
            puts "#{oup}"
        end
    end

    def self.test_merge_3
        inp_1 = [1, 2]
        inp_2 = []
        oup = merge(inp_1, inp_2)
        expected = [1, 2]
        if expected == oup
            puts 'matched'
        else
            puts "#{oup}"
        end
    end

    def self.test_merge_4
        inp_1 = []
        inp_2 = []
        oup = merge(inp_1, inp_2)
        expected = []
        if expected == oup
            puts 'matched'
        else
            puts "#{oup}"
        end
    end

    def self.test_merge_5
        inp_1 = [1, 3, 4, 5, 9]
        inp_2 = [2, 4, 6, 7, 8]
        oup = merge(inp_1, inp_2)
        expected = [1, 2, 3, 4, 4, 5, 6, 7, 8, 9]
        if expected == oup
            puts 'matched'
        else
            puts "#{oup}"
        end
    end

    def self.test_merge_6
        inp_1 = [1, 3, 4, 5, 9, 10]
        inp_2 = [2, 4, 6, 7, 8]
        oup = merge(inp_1, inp_2)
        expected = [1, 2, 3, 4, 4, 5, 6, 7, 8, 9, 10]
        if expected == oup
            puts 'matched'
        else
            puts "#{oup}"
        end
    end

    def self.test_merge_7
        inp_1 = [1, 3, 4, 5, 9]
        inp_2 = [2, 4, 6, 7, 8, 10]
        oup = merge(inp_1, inp_2)
        expected = [1, 2, 3, 4, 4, 5, 6, 7, 8, 9, 10]
        if expected == oup
            puts 'matched'
        else
            puts "#{oup}"
        end
    end

    def self.test_merge_8
        inp_1 = [1, 3, 4, 5, 9, 10]
        inp_2 = [2, 4, 6, 7, 8, 10]
        oup = merge(inp_1, inp_2)
        expected = [1, 2, 3, 4, 4, 5, 6, 7, 8, 9, 10, 10]
        if expected == oup
            puts 'matched'
        else
            puts "#{oup}"
        end
    end
end