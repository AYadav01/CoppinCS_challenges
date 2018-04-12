//Yadav, Anil (Coppin State University)

//package coinFlip;
import java.util.ArrayList;
import java.util.Random;

public class coinFlip {

	public static void main(String[] args) {
		//random number object
		Random rand = new Random();
		
		//this variable will hold the generated random number
		int randomNumber;
		
		//the range of random numbers
		int maxRandom = 84;
		int minRandom = 72;
	
		//threshold point; if number below threshold, it will be assigned 'H' else 'T'
		int threshold = (maxRandom+minRandom)/2;

		//number of iterations
		int num = 100;

		//head and tail counter
		int headCount = 0;
		int tailCount = 0;
		
		//this will hold the final data
		ArrayList<Character> myList = new ArrayList<Character>();
		
		//gathering data
		for (int i = 0; i < num; i++) {	
			randomNumber = rand.nextInt(maxRandom - minRandom + 1) + minRandom;
			if( randomNumber <= threshold ) {
				//add 'H' to the arrayList. (72 is the ASCII representation of H)
				myList.add((char)72);
				headCount++;
			}
			
			else {
				//add 'T' to the arrayList; (84 is the ASCII representation of T)
				myList.add((char)84);
				tailCount ++;
			}	
			//System.out.println("The random number is "+ randomNumber);
		}
		
		//calculating percentage
		double percentHead = (double)(headCount*100)/num;
		double percentTail = (double)(tailCount*100)/num;
		
		//printing output
		System.out.println("Coined is flipped "+num+" times:"+"\n"+myList);
		System.out.println();
		System.out.println("Head appeard "+ headCount+" times and Tail appeard "+tailCount+" times");
		System.out.println();
		System.out.println("Head percentage "+percentHead+"%");
		System.out.println("Tail percentage "+percentTail+"%");
	}
}
