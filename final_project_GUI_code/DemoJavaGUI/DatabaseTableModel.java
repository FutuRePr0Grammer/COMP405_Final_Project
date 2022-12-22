import java.util.ArrayList;

import javax.swing.table.AbstractTableModel;

/**
 * 
 * The GUI table requires a model to define what data appears at each row/column
 */
public class DatabaseTableModel extends AbstractTableModel {
	String[] columnNames = { "Book Name", "Genre", "Author", "ISBN", "Release Date", "Chapter Count" };
	public ArrayList<Row> table = new ArrayList<Row>();
	
	public void setTable(ArrayList<Row> newTable) {
		table = newTable;
	}
	public String getColumnName(int col) {
		return columnNames[col].toString();
	}
	public int getRowCount() { return table.size(); }
	public int getColumnCount() { return columnNames.length; }
	
	public Object getValueAt(int row, int col) {
		if (col == 0) {
			return table.get(row).b_name;
		} else if(col == 1) {
			return table.get(row).g_name;
		} else if(col == 2) {
			return table.get(row).author_name;
		} else if(col == 3){
			return table.get(row).isbn;
		} else if(col == 4){
			return table.get(row).release_date;
		} else {
			return table.get(row).ch_ct;
		}
	}
	public boolean isCellEditable(int row, int col) {
		return false;
	}
	public void setValueAt(Object value, int row, int col) {
	}

}
