
// Class to transfer data from database to GUI table
class Row {
	public String b_name;
	public String g_name;
	public String author_name;
	public String isbn;
	public String release_date;
	public int ch_ct;
	Row(String b_name, String g_name, String author_name, String isbn, String release_date, int ch_ct) {
		this.b_name = b_name;
		this.g_name = g_name;
		this.author_name = author_name;
		this.isbn = isbn;
		this.release_date = release_date;
		this.ch_ct = ch_ct;
	}
}