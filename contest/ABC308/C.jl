function main()
    N = parse(Int, readline())

    ans = Dict()
    input_data = readlines(stdin)
    for i in 1:N
        A, B = parse.(Int, split(input_data[i]))
        p = A // (A + B)  # 有理数として成功率を表現
        if !(p in keys(ans))
            ans[p] = [string(i)]
        else
            push!(ans[p], string(i))
        end
    end

    ans_s = sort(collect(keys(ans)), rev=true)
    ret = [ans[key] for key in ans_s]

    return join(join.(ret, " "), " ")
end

println(main())
