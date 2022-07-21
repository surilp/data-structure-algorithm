package string

import kotlin.math.floor


fun numMatchingSubseq(s: String, words: Array<String>): Int {
    var result = 0
    val sMap = mutableMapOf<Char, ArrayList<Int>>()
    for ((idx, let) in s.withIndex()) {
        val temp = sMap.getOrPut(let) { arrayListOf()}
        temp.add(idx)
    }

    outer@ for (word in words) {
        var currentLocation = -1
        for (let in word) {
            if (sMap.contains(let)) {
                val temp = binarySearch(sMap[let], currentLocation)
                if (temp == -1 || temp == currentLocation) {
                    continue@outer
                } else {
                    currentLocation = temp
                }
            }
            else{
                continue@outer
            }
        }
        result++
    }
    return result
}

fun binarySearch(arr: ArrayList<Int>?, target:Int): Int {
    var result = -1
    if (arr != null) {
        var left = 0
        var right = arr.lastIndex
        while (left <= right) {
            val mid = floor(((left + right) / 2).toDouble()).toInt()

            if (arr[mid] <= target) {
                left = mid + 1
            } else {
                right = mid - 1
                result = arr[mid]
            }
        }
    }
    return result
}


fun main() {
    val input = arrayOf(
        arrayOf("abcde", arrayOf("a", "bb", "acd", "ace")),
        arrayOf("dsahjpjauf", arrayOf("ahjpjau", "ja", "ahbwzgqnuk", "tnmlanowax")),
    )

    input.forEach {
        println(
            "s = ${it[0]}, words = ${it[1]}, result = ${
                numMatchingSubseq(
                    it[0] as String,
                    it[1] as Array<String>
                )
            }"
        )
    }
}