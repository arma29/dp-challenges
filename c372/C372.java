import java.util.ArrayList;
import java.util.Hashtable;
import java.util.Iterator;

public class C372 {

    public static boolean balanced(String str){
        Hashtable<Character, Integer> hash = new Hashtable<Character,Integer>();
        for (int i = 0; i < str.length(); i++) {
            hash.put(str.charAt(i), 
                hash.get(str.charAt(i)) == null ? 0 : hash.get(str.charAt(i)) + 1);
        }
        return hash.get('x') == hash.get('y');
    }

    public static boolean balanced_bonus(String str){
        Hashtable<Character,Integer> hash = new Hashtable<Character,Integer>();
        for (int i = 0; i < str.length(); i++) {
            hash.put(str.charAt(i), 
                hash.get(str.charAt(i)) == null ? 0 : hash.get(str.charAt(i)) + 1);
        }

        Iterator<Integer> it = hash.values().iterator();
        while(it.hasNext()){
            if(hash.get(str.charAt(0)) != it.next())
                return false;
        }
        return true;

        // ArrayList<Integer> array = new ArrayList<Integer>(hash.values());
        // for (int i = 0; i < array.size()-1; i++) {
        //     if(array.get(i) != array.get(i+1))
        //         return false;
        // }
        // return true;
    }
    public static void main(String[] args) {
        System.out.println(balanced("xxxyyy"));
        System.out.println(balanced("xxxyyyy"));
        System.out.println(balanced(""));
        System.out.println(balanced("x"));

        System.out.println(balanced_bonus(""));
        System.out.println(balanced_bonus("x"));
        System.out.println(balanced_bonus("xy"));
        System.out.println(balanced_bonus("xyy"));
        
    }
}