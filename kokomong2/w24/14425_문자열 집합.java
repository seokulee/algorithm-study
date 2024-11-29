#include <algorithm>
#include <iostream>
#include <vector>
#include <map>

using namespace std;

int main(void)
{
	ios::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	int N, M, cnt;;
	string input;
	map<string, int> strmap;

	cin >> N >> M;
	cnt = 0;
	for (int i = 0; i < N; i++)
	{
		cin >> input;
		strmap.insert(make_pair(input, 1));
	}
	for (int i = 0; i < M; i++)
	{
		cin >> input;
		if (strmap.find(input) != strmap.end())
			cnt++;
	}
	cout << cnt;
}
