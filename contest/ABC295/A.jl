test_case = ["and", "not", "that", "the", "you"]


N = parse.(Int, readline())
W = split(readline())

function func(N, W)
    for w in W
        if w in test_case
            return "Yes"
        end
    end
    return "No"
end

println(func(N, W))