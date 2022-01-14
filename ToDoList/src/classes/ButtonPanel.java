package classes;

import javax.swing.*;
import javax.swing.border.Border;
import java.awt.*;

public class ButtonPanel extends JPanel {

    private JButton addTask;
    private JButton clear;

    Border emptyBorder = BorderFactory.createEmptyBorder();

    //Constructor
    ButtonPanel()
    {
        this.setPreferredSize(new Dimension(400, 60));

        addTask = new JButton("Dodaj produkt");
        addTask.setBorder(emptyBorder);
        addTask.setFont(new Font("Sans-serif", Font.PLAIN, 25));

        this.add(addTask);
    }

    public JButton getAddTask()
    {
        return addTask;
    }
}
