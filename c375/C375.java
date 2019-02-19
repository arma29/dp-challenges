import java.util.ArrayList;
import java.util.Scanner;

//javac class.java
//java -cp . class

/*
adj cur adj model example
O has to be: > > or < <
1 has to be: < > or > <

begin 0 has to be: | >
begin 1 has to be: | <
end 0 has to be: < |
end 1 has to be: > |

Tip:
even number of 1 -> impossible
odd number of 1 -> solvable

Algorithm: Iterative Linear Approach (left to right)
flip(String str)
1. check = false, list = null
2. iterate over str:
3.  if check
4.      add(index) at the end of list
5.  else
6.      add(index) at the begin of list
7.  check = check XOR (charAt(index) == 1)
8. return list
*/
public class C375 {

    public static ArrayList<Integer> flip(String str){
        ArrayList<Integer> list = new ArrayList<Integer>();
        boolean check = false;
        for (int i = 0; i < str.length(); i++) {
            if(check){ 
                //maintain the direction, for the next
                //add at the end
                list.add(i);
            }
            else{ 
                //change the direction, for the next
                //add at the begin
                list.add(0,i);
            }
            //Accordly to the video, 1 -> change the direction, while 0 -> keeps.
            //So, its a XOR behavior. 0 doesn't affect.
            check = (str.charAt(i) == '1') ^ (check);
        }

        return check == true ? list : null;
    }

    public static void main(String[] args) {
        
        System.out.println(flip("0100110"));
        System.out.println(flip("0100111"));
    }
}