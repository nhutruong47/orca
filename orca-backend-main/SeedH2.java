import java.sql.*;
import java.util.UUID;
import java.io.File;
import java.nio.file.Files;

public class SeedH2 {
    public static void main(String[] args) throws Exception {
        Class.forName("org.h2.Driver");
        String url = "jdbc:h2:file:C:/Users/TTN/Downloads/orcaktx/orca/orca-backend-main/data/orca-local;AUTO_SERVER=TRUE;MODE=PostgreSQL;DATABASE_TO_UPPER=false;CASE_INSENSITIVE_IDENTIFIERS=TRUE";
        Connection c = DriverManager.getConnection(url, "sa", "12345");
        
        String hash = "$2a$10$3gOAp1BnNUV/b9cbnz6mKejPqXY0qZZtqgiUkGGJCSqCMWGHGbZqe";
        
        // Alter role to VARCHAR
        try {
            c.createStatement().execute("ALTER TABLE users ALTER COLUMN role VARCHAR");
        } catch (Exception e) {}

        // 1. Ensure Manager nguyen.minh.hai
        PreparedStatement checkMgr = c.prepareStatement("SELECT id FROM users WHERE username = ?");
        checkMgr.setString(1, "nguyen.minh.hai");
        ResultSet rsMgr = checkMgr.executeQuery();
        String mgrIdStr;
        if (rsMgr.next()) {
            mgrIdStr = rsMgr.getString("id");
            System.out.println("User nguyen.minh.hai exists.");
        } else {
            mgrIdStr = UUID.randomUUID().toString();
            PreparedStatement insMgr = c.prepareStatement("INSERT INTO users (id, username, password, role, chip_id, locked, full_name, created_at) VALUES (CAST(? AS UUID), ?, ?, 'FACTORY_OWNER', ?, false, ?, CURRENT_TIMESTAMP)");
            insMgr.setString(1, mgrIdStr);
            insMgr.setString(2, "nguyen.minh.hai");
            insMgr.setString(3, hash);
            insMgr.setString(4, "USR-" + UUID.randomUUID());
            insMgr.setString(5, "Nguyễn Minh Hải");
            insMgr.executeUpdate();
            System.out.println("Inserted manager nguyen.minh.hai with password: 1 (wait, the hash is 123456)");
        }
        
        // 2. Run clean_and_seed.sql
        try {
            File file = new File("C:/Users/TTN/Downloads/orcaktx/clean_and_seed.sql");
            if (file.exists()) {
                String sql = new String(Files.readAllBytes(file.toPath()));
                Statement stmt = c.createStatement();
                stmt.execute(sql);
                System.out.println("Executed clean_and_seed.sql");
            }
        } catch (Exception e) {
            System.out.println("Could not run clean_and_seed.sql: " + e.getMessage());
        }

        // 3. Run seed_subscription_customers.sql
        try {
            File file = new File("C:/Users/TTN/Downloads/orcaktx/orca/scripts/seed_subscription_customers.sql");
            if (file.exists()) {
                String sql = new String(Files.readAllBytes(file.toPath()));
                Statement stmt = c.createStatement();
                stmt.execute(sql);
                System.out.println("Executed seed_subscription_customers.sql");
            }
        } catch (Exception e) {
            System.out.println("Could not run seed_subscription_customers.sql: " + e.getMessage());
        }
        
        c.close();
    }
}
