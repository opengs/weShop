package classes;

import javax.swing.*;
import java.awt.*;

public class TitleBar extends JPanel {
    //Constructor
    TitleBar(){
        this.setPreferredSize(new Dimension(400,88));

        JLabel titleText = new JLabel("Lista zakupów");
        titleText.setPreferredSize(new Dimension(300,100));
        titleText.setFont(new Font("Sans-serif", Font.BOLD, 30));
        titleText.setHorizontalAlignment(JLabel.CENTER);

        this.add(titleText);

    }

}
