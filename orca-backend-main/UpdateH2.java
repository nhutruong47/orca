import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;

public class UpdateH2 {
    public static void main(String[] args) {
        try {
            Class.forName("org.h2.Driver");
            String url = "jdbc:h2:file:C:/Users/TTN/Downloads/orcaktx/orca/orca-backend-main/data/orca-local;AUTO_SERVER=TRUE;MODE=PostgreSQL;DATABASE_TO_UPPER=false;CASE_INSENSITIVE_IDENTIFIERS=TRUE";
            Connection conn = DriverManager.getConnection(url, "sa", "12345");
            
            ResultSet rs = conn.createStatement().executeQuery("SELECT * FROM payment_transactions");
            while (rs.next()) {
                System.out.println(rs.getString("txn_ref") + " | " + rs.getString("user_id") + " | " + rs.getString("plan_id"));
            }
            
            conn.close();
            System.out.println("Done.");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
