import java.sql.*;
import java.io.File;
import java.nio.file.Files;

public class SeedH2OnlyClean {
    public static void main(String[] args) throws Exception {
        Class.forName("org.h2.Driver");
        String url = "jdbc:h2:file:C:/Users/TTN/Downloads/orcaktx/orca/orca-backend-main/data/orca-local;AUTO_SERVER=TRUE;MODE=PostgreSQL;DATABASE_TO_UPPER=false;CASE_INSENSITIVE_IDENTIFIERS=TRUE";
        Connection c = DriverManager.getConnection(url, "sa", "12345");
        
        try {
            File file = new File("C:/Users/TTN/Downloads/orcaktx/clean_and_seed.sql");
            if (file.exists()) {
                String sql = new String(Files.readAllBytes(file.toPath()));
                Statement stmt = c.createStatement();
                stmt.execute(sql);
                System.out.println("Executed clean_and_seed.sql successfully.");
            }
        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
        }
        
        c.close();
    }
}
