def birthdayCakeCandles(candles):
    # Write your code here
    srt_candles = sorted(candles)
    count = Counter(srt_candles)
    new_arr = count[srt_candles[-1]]
    return new_arr