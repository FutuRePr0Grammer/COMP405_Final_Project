import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import java.sql.Connection;

import javax.swing.JFrame;
import java.awt.Color;
import javax.swing.JTextField;
import javax.swing.event.TableModelEvent;
import javax.swing.event.TableModelListener;

import java.awt.BorderLayout;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;

import javax.swing.JTable;
import javax.swing.JScrollPane;

public class SQLiteGUIDemo implements KeyListener, TableModelListener {
	// Database connectivity
	Connection connection;
	String sql;
	String DB_PATH = SQLiteGUIDemo.class.getResource("Bookbin.db").getFile();

	// GUI objects
	private JFrame frame;
	private JTable table;
	private JTextField textField;
	private JScrollPane scrollPane;

	// Connect database with table
	DatabaseTableModel tableModel = new DatabaseTableModel();

	/**
	 * Create the application.
	 * @throws SQLException 
	 * @throws ClassNotFoundException 
	 */
	public SQLiteGUIDemo() throws ClassNotFoundException, SQLException {
		// load the sqlite-JDBC driver using the current class loader
		Class.forName( "org.sqlite.JDBC");

		// protocol (jdbc): subprotocol (sqlite):databaseName (Chinook_Sqlite_AutoIncrementPKs.sqlite)
		connection = DriverManager.getConnection("jdbc:sqlite:" + DB_PATH);

		// Initialize GUI
		initializeGUI();

		// Initialize event handlers
		initializeListeners();
	}

	/**
	 * Initialize the contents of the frame.
	 * @throws ClassNotFoundException 
	 * @throws SQLException 
	 */
	private void initializeGUI() throws ClassNotFoundException, SQLException {

		// Setup the main window
		frame = new JFrame();
		frame.setBounds(100, 100, 450, 300);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		//frame.getContentPane().setBackground(Color.pink);
		//frame.setVisible(true);

		// Place the search box at the top
		textField = new JTextField();
		textField.setToolTipText("Search by book name");
		frame.getContentPane().add(textField, BorderLayout.NORTH);
		textField.setColumns(10);

		// Place the table in a scroll pane in the center
		table = new JTable(tableModel);
		table.setBackground(Color.PINK);
		table.setForeground(Color.BLUE);
		table.setGridColor(Color.ORANGE);
		scrollPane = new JScrollPane(table);
		frame.getContentPane().add(scrollPane, BorderLayout.CENTER);
	}

	// Listeners (event handlers) define what to do in response to events.
	// GUIs use on event handlers to bind user actions with computation. 
	private void initializeListeners() {

		// When the user types something, tell the table to update itself
		textField.addKeyListener(this);

		// Define what to do when the table needs to be updated
		// That is, run queries on user input
		// Registering event handler to DatabaseTableModel
		// addTableModelListener need TableModelListener as an argument - used as an Innerclass
		tableModel.addTableModelListener(this);
		
		// Load the table on startup
		tableModel.fireTableDataChanged();
	}
	@Override
	public void keyTyped(KeyEvent e) {}
	@Override
	public void keyPressed(KeyEvent e) {
	}
	@Override
	public void keyReleased(KeyEvent e) {
		// fireTableDataChanged() is a method in AbstractTableModel
		// This method calls tableChanged method
		// This is defined in swing
		// We implement database query to update the table in the tableChanged() method
		tableModel.fireTableDataChanged();
	}
	
	// Whenever the key is released, call this method
	@Override
	public void tableChanged(TableModelEvent e) {
		String param = textField.getText();
		// generate parameterized sql
		/*sql = "SELECT Books.b_name, g_name.g_name" +
				"FROM Books" +
				"JOIN BelongsTo USING (isbn)" +
				"JOIN g_name USING (g_name)" +
				"WHERE Books.b_name LIKE ?";*/
		/*if ( param.equalsIgnoreCase("") ) {*/

		sql = "SELECT b_name, g_name, " +
				"author_name, Books.isbn AS isbn, " +
				"release_date," +
				"ch_ct " +
				"FROM Books " +
				"JOIN BelongsTo ON Books.isbn = BelongsTo.isbn " +
				"JOIN Genre USING (g_id) " +
				"WHERE b_name LIKE ? AND Genre.g_id = BelongsTo.g_id";

		/*sql = "SELECT * " +
				"FROM Books " +
				"JOIN BelongsTo USING (isbn) " +
				"JOIN Genre USING (g_id) " +
				"WHERE Books.b_name LIKE ? AND Genre.g_id = BelongsTo.g_id";*/

		/*} else{
			sql = "SELECT Books.b_name, Genre.g_name" + 
				"FROM Genre" +
				"JOIN BelongsTo USING (g_name)" + 
				"JOIN Books USING (isbn)" + 
				"WHERE Genre.g_name LIKE ?";
		}*/
		// System.out.println("\nSQL: " + sql + "\n");

		try {

			PreparedStatement stmt = connection.prepareStatement( sql );

			if ( !param.equalsIgnoreCase("") ) {
				stmt.setString( 1, "%" + param + "%" );
			}

			// get results
			ResultSet res = stmt.executeQuery();

			// Transfer data from database to GUI
			ArrayList<Row> table = new ArrayList<Row>();
			while ( res.next() ) {
				table.add(new Row(res.getString("b_name"),res.getString("g_name"),
						res.getString("author_name"), res.getString("isbn"),
						res.getString("release_date"), res.getInt("ch_ct")));
			}
			tableModel.setTable(table);

		} catch (Exception e1) {
			e1.printStackTrace();
		}

	}
	/**
	 * Launch the application.
	 * @throws SQLException 
	 * @throws ClassNotFoundException 
	 */
	public static void main(String[] args) throws ClassNotFoundException, SQLException {

		SQLiteGUIDemo window = new SQLiteGUIDemo();
		window.frame.setVisible(true);
	}

}
