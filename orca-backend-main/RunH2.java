import java.sql.*;
import java.util.UUID;

public class RunH2 {
    public static void main(String[] args) throws Exception {
        Class.forName("org.h2.Driver");
        Connection c = DriverManager.getConnection("jdbc:h2:file:C:/Users/TTN/Downloads/orcaktx/orca/orca-backend-main/data/orca-local;AUTO_SERVER=TRUE;MODE=PostgreSQL;DATABASE_TO_UPPER=false;CASE_INSENSITIVE_IDENTIFIERS=TRUE", "sa", "12345");
        
        System.out.println("Deleting old garbage users...");
        int deleted = c.createStatement().executeUpdate("DELETE FROM users WHERE email LIKE 'factory%'");
        System.out.println("Deleted " + deleted + " users.");
        
        String hash = "$2a$10$D26MSIVWtB2CRQaBARdM7uyKBzEbEjNNdb7V5MtOcfsEcCU0jkP8."; // 123456
        String[] names = {"Nguyễn Văn An", "Trần Thị Bích", "Lê Văn Cường", "Phạm Thị Dung", "Hoàng Văn Em"};
        String[] usernames = {"nguyen.van.an", "tran.thi.bich", "le.van.cuong", "pham.thi.dung", "hoang.van.em"};
        String[] emails = {"nguyen.an@gmail.com", "bich.tran@gmail.com", "cuong.le.dev@gmail.com", "pham.dung123@gmail.com", "em.hoang@gmail.com"};
        
        PreparedStatement stmt = c.prepareStatement("INSERT INTO users (id, username, password, role, chip_id, locked, full_name, email, created_at) VALUES (?, ?, ?, 'FACTORY_OWNER', ?, false, ?, ?, CURRENT_TIMESTAMP)");
        
        for (int i = 0; i < names.length; i++) {
            stmt.setString(1, UUID.randomUUID().toString());
            stmt.setString(2, usernames[i]);
            stmt.setString(3, hash);
            stmt.setString(4, "USR-" + UUID.randomUUID().toString());
            stmt.setString(5, names[i]);
            stmt.setString(6, emails[i]);
            stmt.executeUpdate();
        }
        
        System.out.println("Inserted " + names.length + " realistic users.");
        c.close();
    }
}
