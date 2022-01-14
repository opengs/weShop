package classes;


import javax.swing.*;
import java.awt.*;

public class Task extends JPanel {

    private JLabel index;
    private JTextField taskName;
    private JButton done;

    private  boolean checked;

    Task()
    {
        this.setPreferredSize(new Dimension(40,20));
        this.setBackground(Color.red);

        this.setLayout(new BorderLayout());

        checked = false;

        index = new JLabel("");
        index.setPreferredSize(new Dimension(35,20));
        index.setHorizontalAlignment(JLabel.CENTER);
        index.setFont(new Font("Sans-serif", Font.PLAIN, 25));
        this.add(index, BorderLayout.WEST);

        taskName = new JTextField("Wpisz nazwę produktu...");
        taskName.setBorder(BorderFactory.createEmptyBorder());
        taskName.setFont(new Font("Sans-serif", Font.PLAIN, 20));
        taskName.setBackground(Color.red);

        this.add(taskName,BorderLayout.CENTER);

        done = new JButton("Do koszyka");
        done.setPreferredSize(new Dimension(70,20));
        done.setBorder(BorderFactory.createEmptyBorder());

        this.add(done,BorderLayout.EAST);
    }
    public JButton getDone()
    {
        return done;
    }
    public void changeIndex(int num)
    {
        this.index.setText(num+"");
        this.revalidate();
    }

    public void changeState()
    {
        this.setBackground(Color.green);
        taskName.setBackground(Color.green);
        checked = true;
    }
}
