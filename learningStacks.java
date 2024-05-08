import java.util.Stack;

public class learningStacks{
    public static void main(String[] args) {
        
        /*Stacks are Last-In First-Out

          Think of a "vertical tower"

          push() to add to the top
          pop() to remove from the top

        */

        Stack<String> myStack = new Stack<String>();

        System.out.println(myStack.empty()); //empty() returns boolean

        myStack.push("GTA V");
        myStack.push("Fortnite");
        myStack.push("Valorant"); //push() adds items to the stack
        
        System.out.println(myStack);

        String removed = myStack.pop(); //pop() removes last added item and also can be used to store that

        System.out.println(myStack);
        System.out.printf("The game removed was %s.\n", removed);

        System.out.println(myStack.peek()); //peak() returns the topmost item without removing

        System.out.println(myStack.search("GTA V")); //search() returns index starting at 1, -1 if not in stack.
    
        /* Uses of stacks

           1. undo/redo features in text editors
           2. moving back/forward through browser history
           3. backtracking algorithms (maze, file directories)
           4. calling functions (call stack)

         */
    
    }
}