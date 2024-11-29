import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Main {
	static class TrieNode{
		Map<Character, TrieNode> childNode = new HashMap<>();
		boolean terminal;
		
		public TrieNode(){
			/* no-op */
		}
		
		public void insert(String word) {
			TrieNode trieNode = this;
			for(int i=0; i<word.length(); i++) {
				char c = word.charAt(i);
				
				trieNode.childNode.putIfAbsent(c, new TrieNode());
				trieNode = trieNode.childNode.get(c);
				
				if(i==word.length()-1) {
					trieNode.terminal = true;
				}
			}
		}
		
		public int autoModule(String word) { 
			TrieNode trieNode = this;
			int cnt=0;
			for(int i=0; i<word.length(); i++) {
				char c= word.charAt(i);
				TrieNode node = trieNode.childNode.get(c);
				if(i==0) {
					cnt++;
				}
				else if(trieNode.terminal || trieNode.childNode.size()>1) {
					cnt++;
				}
				trieNode = node;
			}
			return cnt;
		}
	}
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));	
		String line;
		while((line = br.readLine())!=null) {
			try {
				int n = Integer.parseInt(line);
				List<String> inputData = new ArrayList<>();
				TrieNode trie = new TrieNode();
				for(int i=0; i<n; i++) {
					String str = br.readLine();
					inputData.add(str);
					trie.insert(str);
				}
				double res=0;
				for(String str : inputData) {
					res+= trie.autoModule(str);	
				}
				System.out.println(String.format("%.2f",res/inputData.size()));
			}catch(NumberFormatException e) {
				return;
			}
		}
	}
}