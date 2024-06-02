import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;
import java.util.TreeSet;

public class Main {

	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;

		// INIT size, set of meeting time, count of quick meeting(startTime == endTime)'s
		int size = Integer.parseInt(br.readLine());
		TreeSet<Long> meetings = new TreeSet<>();
		Map<Integer, Integer> cntQuickMeetings = new HashMap<>(); // key: time, value: count
		for (int i = 0; i < size; i++) {
			st = new StringTokenizer(br.readLine());
			int startTime = Integer.parseInt(st.nextToken());
			int endTime = Integer.parseInt(st.nextToken());

			long longValue = ((long) endTime << 32) + startTime;
			meetings.add(longValue);

			if (startTime == endTime)
				cntQuickMeetings.put(endTime, cntQuickMeetings.containsKey(endTime) ? cntQuickMeetings.get(endTime) + 1 : 1);
		}

		// CALC
		int result = 0;
		int latestEndTime = 0;
		for (long longValue : meetings)
		{
			int startTime = (int) (longValue & ((1L << 32) - 1));
			int endTime = (int) (longValue >> 32);

			if (latestEndTime <= startTime && latestEndTime <= endTime) {
				latestEndTime = endTime;

				result += (startTime == endTime) ? cntQuickMeetings.get(endTime) : 1;
			}
		}
		
		// PRINT
		System.out.println(result);

	}

}