package 그래프와순회.실버.너비우선탐색2_24445;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static int[] arr;
    public static List<List<Integer>> list = new ArrayList<>();
    public static int count = 1;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int r = Integer.parseInt(st.nextToken());

        arr = new int[n + 1];

        for (int i = 0; i <= n; i++) {
            list.add(new ArrayList<>());
        }

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            list.get(a).add(b);
            list.get(b).add(a);
        }

        for (List<Integer> integers : list) {
            Collections.sort(integers, Collections.reverseOrder());
        }

        dfs(r);
        for (int i = 1; i <= n; i++) {
            System.out.println(arr[i]);
        }

    }

    public static void dfs(int start) {
        Queue<Integer> q = new LinkedList<>();

        q.offer(start);
        arr[start] = count++;

        while (!q.isEmpty()) {
            int a = q.poll();

            for (int v : list.get(a)) {
                int next = v;

                if (arr[v] != 0) {
                    continue;
                }
                q.offer(next);
                arr[next] = count++;
            }
        }
    }
}
