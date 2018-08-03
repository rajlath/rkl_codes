func solution(heights: [Int], length: Int) -> Int {
    var stack = [Int]()
    var numberBlocks = 0

    for height in heights {
        if stack.isEmpty || stack.last > height {
            while stack.last > height {
                stack.removeLast()
            }

            if stack.last != height {
                stack.append(height)
                numberBlocks++
            }
        }
    }

    return numberBlocks
}