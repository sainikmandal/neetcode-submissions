func groupAnagrams(strs []string) [][]string {
    fMap := make(map[[26]int][]string)
    for _, str := range strs {
        var count[26]int
        for _, char := range str{
            if char >= 'a' && char <= 'z' {
                count[char - 'a']++
                }
        }
         fMap[count] = append(fMap[count], str)
    }

    result := make([][]string, 0, len(fMap))

    for _, group := range fMap {
        result = append(result, group)
    }

    return result
}
