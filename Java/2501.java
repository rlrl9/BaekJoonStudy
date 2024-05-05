import java.io.IOException;
import java.util.ArrayList;
import java.util.Scanner;

class Main{
	public static void main(String[] args) throws IOException {
		Scanner sc = new Scanner(System.in);
		ArrayList<Integer> list = new ArrayList<>();
		int a= sc.nextInt();
		int b = sc.nextInt();
        int res=0;
        for(int i=1;i<=a;i++) {
        	if (a % i ==0){
        		list.add(i);
        	}
        	if(list.size()==b) {
        		res= i;
        		break;
        	}
        }
        System.out.println(res);
        
	}
}
