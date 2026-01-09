class Pair{
    int node;
    int distance;
    public Pair(int node,int distance){
        this.node = node;
        this.distance = distance;
    }
}

class Solution {
    public int networkDelayTime(int[][] times, int n, int k) {
        ArrayList<ArrayList<Pair>> adj = new ArrayList<>();
        for(int i=0;i<=n;i++){
            adj.add(new ArrayList<>());
        }
        for(int i=0;i<times.length;i++){
            adj.get(times[i][0]).add(new Pair(times[i][1],times[i][2]));
        }

        PriorityQueue<Pair> pq = new PriorityQueue<>((a,b)->(a.distance-b.distance));
        pq.add(new Pair(k,0));

        int dist[]  = new int[n+1];
        Arrays.fill(dist,Integer.MAX_VALUE);
        dist[0] = 0;
        dist[k] = 0;

        while(!pq.isEmpty()){
            Pair curr = pq.remove();
            int src = curr.node;
            int distance = curr.distance;

            for(Pair nbr:adj.get(src)){
                int d  = nbr.distance;
                int x  = nbr.node;
                if(distance+d < dist[x]){
                    dist[x] = distance + d;
                    pq.add(new Pair(x,dist[x]));
                }
            }
        }
        int ans = Integer.MIN_VALUE;
        for(int i=0;i<=n;i++){
            if(dist[i]==Integer.MAX_VALUE) return -1;
            else ans = Math.max(ans,dist[i]);
        }
        
        return ans;

    }
}