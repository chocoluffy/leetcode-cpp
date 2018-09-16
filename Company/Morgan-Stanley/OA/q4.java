public class EnhancedFor{
    public static void main(String[] args){
        byte arr[]=new byte[]{2,3,4,5};
       for(final int i : getCharArray(arr))
           System.out.print(i+" ");
   }
   static char[] getCharArray(byte[]arr){
       char[] carr=new char[4];
       int i=0;
        for(byte c : arr){
            carr[i]=(char)c++;
            i++;
        }
        return carr;
    }
 }

 public class IkmTest {
    public IkmTest() {
        this(10);
    }
    public IkmTest(int data) {
        this.data = data;
    }
    void display() {
        System.out.println("data = " + data);
    }
    int data;
   
class Decrementer {
    public void decrement(double data) {
        data = data - 1.0;
    }
}    
   
    public static void main (String [] args) {
        int data = 0;
        IkmTest t = new IkmTest(data);
        IkmTest.Decrementer d = t.new Decrementer();
        d.decrement(data);
        t.display();
    }
}