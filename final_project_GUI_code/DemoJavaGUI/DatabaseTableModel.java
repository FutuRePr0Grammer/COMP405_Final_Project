import java.util.ArrayList;

import javax.swing.table.AbstractTableModel;

/**
 * 
 * The GUI table requires a model to define what data appears at each row/column
 */
public class DatabaseTableModel extends AbstractTableModel {
	String[] columnNames = { "b_name", "g_id" };
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
		} else {
			return table.get(row).g_id;
		}
	}
	public boolean isCellEditable(int row, int col) {
		return false;
	}
	public void setValueAt(Object value, int row, int col) {
	}

}
